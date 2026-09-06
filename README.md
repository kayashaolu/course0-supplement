# Course 0 starter repo

This is a small job queue and worker, written in plain Python. It is small
on purpose: small enough that you can read the whole thing before your
junior engineer, the AI coding agent, ever touches it. The course lab
hands that agent two well-scoped tasks to run against this code.

## Where the code lives

- `src/queue.py`: a minimal first-in, first-out `Queue`.
- `src/worker.py`: a `Worker` that drains a `Queue`, calling a
  `process(job)` function you supply for each job.
- `src/cli.py`: a small demo. It enqueues 9 jobs, drains them, and prints
  successes and failures.
- `test/`: the test suite. Green on a fresh clone, before you touch
  anything.

No `pip install` step: this repo has zero runtime dependencies, so
there is nothing to fetch and nothing that can drift between when this was
written and when you cloned it.

```bash
python3 -m src.cli                              # runs the demo CLI
python3 -m unittest discover -s test -t .        # runs the test suite (stdlib unittest, no test framework installed)
```

## The two tasks

Your two tasks come from the course, not this repo. Lab 1 and Lab 2 hand them
to you directly. That's deliberate: on a real team the task doesn't live in
the codebase either.

## Setup

This repo is meant to be run with [scaffold](https://github.com/kayashaolu/systemthinkinglab)
mentoring your AI coding agent through each task: plan first, then build,
then write down what it learned in a wiki that compounds.

Claude Code needs Node >= 22. Then, inside Claude Code:

```
/plugin marketplace add kayashaolu/systemthinkinglab
/plugin install scaffold@systemthinkinglab
```

Your first run of `/scaffold` creates a `scaffold-wiki/` folder. Its defaults
are the ones this course uses (the second agent is called the breaker; the
direction-mode ceiling is ten rounds and sixty minutes), so there is nothing
to configure before Lab 2.

## The sizing test

Lab 2's task, the dead-letter path, is the worked example: you run the
sizing test on it yourself, criterion by criterion, before handing it to
your junior engineer unsupervised in direction mode. Lab 1's task, retry
with backoff, passes the same test. Course 0 keeps you in the loop for it
on purpose, in craft mode, so you see the plan conversation before you
ever step outside it. This rule is also taught in Course 0 itself: if the
wording below does not match the lesson you were given, the lesson wins.
Flag the mismatch.

A task is small enough to hand your junior engineer unsupervised when all
four of these are true:

1. Done in one sentence, no "and."
2. Checkable in five minutes: one command, one output.
3. At most one decision worth arguing about.
4. No money, no auth, no data you can't restore, no service you don't
   control.

## Read the code first

Before you hand either task from the lab to your engineer, look through
the code yourself and see if you can come up with your own plan for the
ask. Then you have your own plan to compare the agent's against. It works
best this way.

Then go back to the lab in the course for the actual instructions, and let
scaffold guide the rest from there.

## If something does not work

If a setup step does not work for you, that's useful signal, not a
you-problem. Tell us about it.
