import os
import yaml
import click
from rich import print
from steem import Steem
from steem.commit import Commit


wif = os.environ.get("STEEMIT_POSTING_KEY")
if wif is None:
    print("STEEMIT_POSTING_KEY is a required environment variable")
    exit(1)

steem = Steem()
commit = Commit(steemd_instance=steem, unsigned=True, keys=[wif])


@click.group()
def main():
    pass


@main.command()
@click.argument("file", type=click.File('r'))
def post(file):
    content = file.read()
    # remove frontmatter
    _, front, content = content.split("---")
    front = yaml.load(front.strip(), Loader=yaml.SafeLoader)
    content = content.strip()
    tags = front.get("tags")
    if not isinstance(tags, list):
        tags = tags.split(" ")
    tx = commit.post(
        front["title"],
        "body",
        "chainsquad",
        json_metadata={},
        comment_options = {
            'max_accepted_payout': '1000000.000 SBD',
            'percent_steem_dollars': 0,
            'allow_votes': True,
            'allow_curation_rewards': True,
            'extensions': []
        },
        tags=tags,
        self_vote=True
    )
    print(tx)


if __name__ == "__main__":
    main()
