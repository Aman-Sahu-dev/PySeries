import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "scores.json"


def load_games() -> list[dict]:
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r") as file:
        return json.load(file)


def save_game(won: bool, attempts: int) -> None:
    games = load_games()

    games.append({
        "won": won,
        "attempts": attempts
    })

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w") as file:
        json.dump(games, file, indent=4)


def get_statistics() -> dict:
    games = load_games()

    wins = [game for game in games if game["won"]]
    losses = [game for game in games if not game["won"]]

    winning_attempts = [game["attempts"] for game in wins]

    return {
        "total_games": len(games),
        "wins": len(wins),
        "losses": len(losses),
        "high_score": min(winning_attempts, default=None),
        "average_attempts": (
            round(sum(winning_attempts) / len(winning_attempts), 2)
            if winning_attempts else 0
        ),
        "highest_attempts": max(winning_attempts, default=0)
    }
