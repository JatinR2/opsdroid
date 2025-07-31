# Release Notes - v1.0.0

*Released on 2024-05-15*

## Summary
This release, v1.0.0, brings significant advancements in connector capabilities, particularly for Mattermost and Slack, alongside crucial bug fixes and substantial internal tooling enhancements. Key new features include a re-implemented Mattermost connector with full threading support, emoji reaction processing, and improved websocket event filtering. The Slack connector now supports file uploads and interactive Modals. The Matrix connector has also seen improvements in event handling. A new contact-manager skill with SQLite integration has been added, and the project now supports ARM builds. On the stability front, numerous CI pipeline issues have been resolved, ensuring more reliable development workflows. A notable change for users is the discontinuation of official support for Python 3.7, requiring an upgrade to newer Python versions. This release also marks a strategic shift to Poetry for dependency management, accompanied by various tooling and CI configuration cleanups, setting the stage for more streamlined future development.

## ✨ New Features
- Added support for multiple regex matches.
- Improved Mattermost connector with proper filters for websocket events.
- Added an optional setting to the Mattermost Connector to process messages with specific emoji reactions.
- Enabled Mattermost bots to respond within threads.
- Re-implemented the Mattermost connector for improved functionality and stability.
- Introduced a new contact-manager skill with SQLite integration.
- Switched to using the Python OLM package.
- Added handling for `LeaveRoom` events in the Matrix connector.
- Added support for ARM builds.
- Added a handler for file uploads in the Slack connector, and updated the async test runner plugin and documentation parser.
- Configured the web server to use TLS 1.2 protocol for SSL context.
- Implemented reporting of unhandled exceptions as warnings.
- Added a retry timer for Slack API rate limit thresholds and enabled the ability to reply to other bots and within a thread using Blocks.
- Added support for Rasa entity extraction with roles.
- Added compatibility with Rasa versions 3.x and above.
- Added an auto mode for Pytest.
- Added middleware to `aiohttp` server to handle CORS requests.
- Added a CLI option to print the configuration file path.
- Implemented small improvements to the websocket connector.
- Enabled simple logging when running in a non-interactive shell.
- Implemented the command center backend.
- Added ability to search Slack Channel ID by name.
- Added Modal Feature to the Slack Connector.
- Added the initial websocket connector.
- Improved the Mattermost connector.
- Enhanced Matrix connector to include reactions in message events.
- Enhanced Matrix connector to use `message.respond` for replying to messages.
- Enhanced Matrix connector to also include replies to the bot's own messages.

## 🐛 Bug Fixes
- Fixed CI build issues by adjusting supported Python versions and updating incompatible dependencies.
- Fixed an issue by setting Notepad as the default editor for Windows systems.
- Fixed an issue with Matrix connector proxy configuration.
- Improved handling for brittle `caplog` checks.
- Fixed issue #1784 by adding a 'filesize' parameter.
- Fixed issue #1737 to ensure '@' characters are retained when replacing usernames.
- Fixed the currently broken Facebook connector.
- Improved Matrix event creation by raising an exception if a request fails.
- Fixed a Mongo database error.
- Fixed an issue in the Matrix specification where `filter_id` was incorrectly treated as an integer instead of a string.
- Corrected `EditedMessage` handling in Slack connector to use 'username' as 'user' is not consistently present in API responses.
- Fixed a broken test.
- Fixed Versioneer detection issues.
- Fixed CI errors.
- Fixed a configuration sample entry.
- Fixed Tox Docker run in CI.
- Improved Rasa NLU connector to return a proper error when Rasa is not reachable.
- Fixed Rasa NLU connector to prevent encoding intents to ASCII.
- Fixed CI by increasing the timeout for macOS tests.
- Replaced 'whitelist' with 'allowlist' to fix CI issues.
- Resolved various CI failures.
- Fixed CI and a potential bug in the loader.
- Fixed channel count when retrieving channels from Slack.
- Fixed documentation URLs.
- Fixed `KeyErrors` on messages without text.
- Fixed all broken tests for the command center backend.
- Fixed Mattermost connector to correctly parse reaction remove events (issue #1916).
- Fixed flaky tests.
- Added a missing dependency to `setup.cfg`.
- Fixed the release drafter action.
- Fixed Python version in Docker build.
- Fixed Matrix connector to only reply to messages in the current room.

## ⚡ Performance Improvements
- No performance improvements in this release.

## 💥 Breaking Changes
- Dropped official support for Python 3.7.

## 📝 Other Changes
- Updated release drafter configuration.
- Converted `test_message.py` from unittest to pytest framework.
- Applied fixes and improvements to the Slack Connector documentation.
- Updated `example_configuration.yaml` with an example for Matrix access token.
- Updated `jinja2` dependency from 3.1.3 to 3.1.4.
- Relaxed code coverage requirements.
- Removed unused `websockets` dependency.
- Updated `jinja2` dependency from 2.11.3 to 3.1.3.
- Applied small fixes to the Matrix connector documentation.
- Updated labeler configuration.
- Updated Versioneer.
- Updated Python and Alpine base images.
- Fixed a typo in Rasa NLU documentation.
- Corrected Rasa port in Docker run command documentation.
- Updated the `emoji` package to version 2.1.0.
- Migrated CI system from Jenkins to GitHub Actions.
- Added Python 3.10 to the environment list in `tox.ini`.
- Configured Docker development tag builds from `main`/`master` branch on each commit.
- Removed old command center frontend files.
- Removed unneeded logging from the Matrix connector.
- Updated `actions/setup-python` GitHub Action.
- Moved release-drafter configuration.
- Updated release drafter configuration.
- Updated `pygments` dependency from 2.11.2 to 2.12.0.
- Updated `requests` dependency from 2.27.1 to 2.28.0.
- Configured tests to run on Python 3.10.
- Adjusted documentation build process to only create docs on the `main` branch.
- Removed pre-commit checks.
- Removed old test environment configurations.
- Updated CI to run on Python 3.10.
- Upgraded various dependencies.
- Upgraded `black` formatter.
- Removed old test command.
- Switched dependency management and build system to Poetry.
- Refactored tests to support `poetry run`.
- Moved `tox.ini` configuration into `pyproject.toml`.
- Updated `click` dependency from 8.0.4 to 8.1.3.
- Updated `aiohttp` dependency from 3.8.1 to 3.8.3.
- Updated `packaging` dependency (minor update).
- Updated `actions/checkout` GitHub Action.
- Updated CI documentation build process.
- Stopped running old pre-commit checks.
- Updated `codecov/codecov-action` from version 2 to 3.
- Updated `actions/cache` GitHub Action.
- Upgraded build action.
- Added Python versions to the documentation workflow.
- Updated workflow permissions.
- Set correct permissions for GitHub Actions.
- Split PR and push workflows for CI.
- Cleaned up CI workflows.
- Updated `pillow` dependency from 9.0.1 to 9.1.0.
- Updated `matrix-nio` dependency from 0.18.0 to 0.18.1.
- Reverted 'Update issue templates'.
- Updated issue templates.
- Updated issue forms.
- Added `pull_request_template.md`.

## 👥 Contributors
Thank you to all contributors who made this release possible:
- @pyup.io bot (435 commits)
- @Jacob Tomlinson (333 commits)
- @Fábio Rosado (103 commits)
- @Stuart Mumford (33 commits)
- @chillipeper (16 commits)
- @Ajit D'Sa (12 commits)
- @Oleg Fiksel (12 commits)
- @dependabot[bot] (8 commits)
- @Daniccan VP (7 commits)
- @Hicham Terkiba (7 commits)
- @Juan A (7 commits)
- @Tyagdit (7 commits)
- @Drew Leonard (6 commits)
- @anxodio (6 commits)
- @MrNaif2018 (5 commits)
- @Oleg Butuzov (5 commits)
- @aboukhal (5 commits)
- @George Panges - Tseres (4 commits)
- @Gergely Polonkai (4 commits)
- @Jacob Floyd (4 commits)
- @John Kristensen (4 commits)
- @Krishna Kumar (4 commits)
- @Rex Roof (4 commits)
- @Sagar Mehar (4 commits)
- @David DR (3 commits)
- @Dudley (3 commits)
- @Haardik Dharma (3 commits)
- @Hritwik (3 commits)
- @Ian (3 commits)
- @Levente Csőke (3 commits)
- @Michael Albert (3 commits)
- @Sleuth56 (3 commits)
- @Suprith Kumar Suvarneshwar (3 commits)
- @Tony Garcia (3 commits)
- @jos3p (3 commits)
- @oleg-fiksel (3 commits)
- @rr3khan (3 commits)
- @Aayush Bisen (2 commits)

## 📊 Release Statistics
- Total commits: 792
- Contributors: 43
- Files changed: Not available
