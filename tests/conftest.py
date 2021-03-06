from __future__ import absolute_import, print_function

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest
from flask import Flask
from flask_taxonomies.proxies import current_flask_taxonomies
from flask_taxonomies.term_identification import TermIdentification
from invenio_db import InvenioDB
from invenio_db import db as db_
from sqlalchemy_utils import database_exists, create_database, drop_database

from oarepo_taxonomies.ext import OarepoTaxonomies


@pytest.yield_fixture()
def app():
    instance_path = tempfile.mkdtemp()
    app = Flask('testapp', instance_path=instance_path)

    # os.environ["INVENIO_INSTANCE_PATH"] = instance_path

    app.config.update(
        SQLALCHEMY_TRACK_MODIFICATIONS=True,
        SERVER_NAME='127.0.0.1:5000',
        INVENIO_INSTANCE_PATH=instance_path,
        DEBUG=True,
        FLASK_TAXONOMIES_URL_PREFIX='/2.0/taxonomies/'  # in tests, api is not on /api but directly in the root
    )
    print(os.environ.get("INVENIO_INSTANCE_PATH"))

    InvenioDB(app)
    OarepoTaxonomies(app)
    with app.app_context():
        # app.register_blueprint(taxonomies_blueprint)
        yield app

    shutil.rmtree(instance_path)


@pytest.fixture
def db(app):
    """Create database for the tests."""
    dir_path = os.path.dirname(__file__)
    parent_path = str(Path(dir_path).parent)
    db_path = os.environ.get('SQLALCHEMY_DATABASE_URI', f'sqlite:////{parent_path}/database.db')
    os.environ["INVENIO_SQLALCHEMY_DATABASE_URI"] = db_path
    app.config.update(
        SQLALCHEMY_DATABASE_URI=db_path
    )
    if database_exists(str(db_.engine.url)):
        drop_database(db_.engine.url)
    if not database_exists(str(db_.engine.url)):
        create_database(db_.engine.url)
    db_.create_all()
    subprocess.run(["invenio", "taxonomies", "init"])
    yield db_

    # Explicitly close DB connection
    db_.session.close()
    db_.drop_all()


@pytest.fixture
def client(app, db):
    from flask_taxonomies.models import Base
    Base.metadata.create_all(db.engine)
    return app.test_client()


@pytest.fixture
def tax_url(app):
    url = app.config['FLASK_TAXONOMIES_URL_PREFIX']
    if not url.endswith('/'):
        url += '/'
    return url


@pytest.fixture
def taxonomy(app, db):
    taxonomy = current_flask_taxonomies.create_taxonomy("test_taxonomy", extra_data={
        "title":
            {
                "cs": "test_taxonomy",
                "en": "test_taxonomy"
            }
    })
    db.session.commit()
    return taxonomy


@pytest.fixture
def taxonomy_tree(app, db, taxonomy):
    id1 = TermIdentification(taxonomy=taxonomy, slug="a")
    term1 = current_flask_taxonomies.create_term(id1, extra_data={"test": "extra_data"})
    id2 = TermIdentification(parent=term1, slug="b")
    term2 = current_flask_taxonomies.create_term(id2, extra_data={"test": "extra_data"})
    id3 = TermIdentification(taxonomy=taxonomy, slug="a/b/c")
    term3 = current_flask_taxonomies.create_term(id3, extra_data={"test": "extra_data"})
    db.session.commit()
