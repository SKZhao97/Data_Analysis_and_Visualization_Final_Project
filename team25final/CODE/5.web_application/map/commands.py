import click
from map import app, db
from map.models import User, Trip

@app.cli.command()  
@click.option('--drop', is_flag=True, help='Create after drop.') # Init database
def initdb(drop):
    """Initialize the database."""
    if drop:  
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  