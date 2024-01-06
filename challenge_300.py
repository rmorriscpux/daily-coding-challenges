'''
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the top 3 candidates at any given time.
If you find a voter voting more than once, report this as fraud.
'''

from random import randint, shuffle

class VoterFraudException(Exception):
    pass

class VotingCounter:
    def __init__(self, vote_file: str):
        self._vote_file = vote_file
        self._voters = set()
        self.vote_count = dict()

    @property
    def top_3(self) -> list:
        leaderboard = sorted(self.vote_count.items(), key=lambda c: c[1], reverse=True)[:3]
        return [candidate[0] for candidate in leaderboard]
    
    @property
    def total_votes(self) -> int:
        return sum(self.vote_count.values())
    
    def readVotes(self, start_line: int=0, num_lines: int=-1) -> int:
        votes = []
        if start_line < 0:
            start_line = 0
        # Read in the votes from the file stream.
        with open(self._vote_file) as vf:
            votes = vf.readlines()[start_line:] if num_lines < 0 else vf.readlines()[start_line:start_line+num_lines]
        # Count votes for each candidate.
        for v in votes:
            voter_id, candidate_id = v.removeprefix('(').removesuffix(')\n').split(', ')
            # Voter already found in self._voters
            if voter_id in self._voters:
                raise VoterFraudException(f"Voter '{voter_id}' counted twice!")
            if candidate_id not in self.vote_count:
                self.vote_count[candidate_id] = 0
            self.vote_count[candidate_id] += 1
            self._voters.add(voter_id)
        return len(votes)

# Generate a randomized voter pool and write into a text file.
def voteGenerator(out_file: str, vote_count: int=100000, candidate_count: int=10):
    voter_order = list(range(vote_count))
    shuffle(voter_order)
    with open(out_file, 'w') as writer:
        for voter_id in voter_order:
            writer.write(f"({voter_id}, {randint(1, candidate_count)})\n")
    return

if __name__ == "__main__":
    VOTE_FILE = 'challenge_300.txt'

    voteGenerator(VOTE_FILE)

    tally = VotingCounter(VOTE_FILE)
    tally.readVotes(0, 50000)
    print(tally.top_3)
    print(tally.vote_count, tally.total_votes)
    tally.readVotes(50000, 50000)
    print(tally.top_3)
    print(tally.vote_count, tally.total_votes)