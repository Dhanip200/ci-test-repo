# ci-test-repo

Test repo for the Self-Healing CI/CD Agent.

Contains a deliberate bug in `src/calculator.py` — `find_max` uses `<` instead of `>`,
so it returns the minimum instead of the maximum. The CI workflow will fail, and the
healing agent will detect the failure, read the code, and open a fix PR automatically.
