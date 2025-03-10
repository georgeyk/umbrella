import marimo

__generated_with = "0.11.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import sys
    import marimo as mo
    return mo, sys


@app.cell
def _(mo):
    mo.md("""# a cli test""")
    return


@app.cell
def _(mo, sys):
    if mo.app_meta().mode != "script":
        print("not running as a script")
        sys.exit(1)
    return


@app.cell
def _(mo):
    args = mo.cli_args()
    print(args)
    return (args,)


if __name__ == "__main__":
    app.run()
