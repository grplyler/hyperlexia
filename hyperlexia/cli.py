import click
from .lib import *
from .log import log
from . import config
from .methods import textrank


@click.group()
def cli():
    pass

# Create a Proxypass site
@click.command(help="Summarize written content in a text files")
@click.argument('filename')
@click.option('-m', '--method', help="Summarization Method/Algorithm", default="textrank")
@click.option('-t', '--top', help="Length of summary", default=5, type=int)
@click.option('-p', '--percent', help="Percent of reduction", default=-1, type=int)
def summarize(filename, method, top, percent):
    # log.info(f"Summarizing {filename} with length of {top}")
    
    if method == 'textrank' or method == 'tr':
        textrank.generate_summary(filename, top, percent)


cli.add_command(summarize)
