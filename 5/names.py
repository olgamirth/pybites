import typer

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

app = typer.Typer()


@app.command()
def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    seen = set()
    titled_deduped_names = [name.title() for name in names if not
                            (name.lower() in seen or seen.add(name.lower()))]
    return titled_deduped_names


@app.command()
def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    sorted_names = sorted(names, key=lambda x: x.split()[-1], reverse=True)
    return sorted_names


@app.command()
def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    first_names = [name.split()[0]for name in names]
    return min(first_names, key=len)


