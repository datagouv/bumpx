from bumpx.forge import BaseForge, GitHub


class BaseForgeTest:
    def test_execute_verbose(self, mocker):
        forge = BaseForge(verbose=True)
        execute = mocker.patch("bumpx.forge.execute")
        forge.execute("cmd arg")
        execute.assert_called_with("cmd arg", verbose=True)

    def test_execute_quiet(self, mocker):
        forge = BaseForge(verbose=False)
        execute = mocker.patch("bumpx.forge.execute")
        forge.execute("cmd arg")
        execute.assert_called_with("cmd arg", verbose=False)


class GitHubTest:
    def test_release(self, mocker):
        github = GitHub()

        execute = mocker.patch.object(github, "execute")
        github.release(version="fake")
        execute.assert_called_with(["gh", "release", "create", "fake", "--title", "fake"])

    def test_release_with_notes(self, mocker):
        github = GitHub()

        execute = mocker.patch.object(github, "execute")
        github.release(version="fake", notes="some notes")
        execute.assert_called_with(
            ["gh", "release", "create", "fake", "--title", "fake", "--notes", "some notes"]
        )
