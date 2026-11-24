import os

# One-line office joke for "Make the AI Judge Laugh: Office Jokes".
# The program writes exactly that one line, nothing else, to entry.txt.
# The grader sets MAKEFUN_OUTPUT_DIR to /output; locally it falls back
# to /output so the same code runs unchanged in both places.

JOKE = "I replied-all to say 'please remove me from this thread' and now the thread is 47 emails long, all of them asking to be removed."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
