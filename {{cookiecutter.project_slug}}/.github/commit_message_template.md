[type](scope)!: description

body

footers

<!--
type (required): one or more of the bellow keywords:
    - fix: patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
    - feature: introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
    - devops:
    - docs: changes to the documentation.
    - style: formatting, missing semi colons, etc; no production code change.
    - refactor: refactoring production code, eg. renaming a variable.
    - perf: optimizes perfomence
    - test: adding missing tests, refactoring tests; no production code change.
    - chore: makes a change that doesn't
    - ... and others. The list isn't exhaustive.
scope (optional): can be empty (e.g. if the change is a global or difficult to assign to a single component), in which
    case the parentheses are omitted.
exclamation mark (optional): a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope,
    introduces a breaking API change (correlating with MAJOR in Semantic Versioning).
description (required): short, one-line description.
body (optional): gives more detailed description. It can be a list of changes made.
footers (optional): lists a set of tokens in `git trailer` format and/or other info, like:
    - BREAKING CHANGE warning (correlating with MAJOR in Semantic Versioning).
    - `Fixes #123` token for GitHub issue automation.

The template follows [Conventional Commits Standard v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/). If you
are searching for more details and examples, have a look there.
-->
