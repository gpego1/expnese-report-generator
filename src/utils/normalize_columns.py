import pandas as pd
COLUMN_POSSIBLES = {
    "data": ["data", "date", "dt", "dt_lancamento"],
    "descricao": ["descricao", "descrição", "description", "historico"],
    "valor": ["valor", "amount", "preco", "preço"],
    "categoria": ["categoria", "category", "tag"],
}


def resolve_columns(df, possibles):
    return next((p for p in possibles if p in df.columns), None)


def normalize_columns(df: pd.DataFrame):
    missing = []
    rename_map = {}

    for default_name, possibles in COLUMN_POSSIBLES.items():
        column = resolve_columns(df, possibles)
        if column == None:
            missing.append(column)
        elif column == default_name:
            rename_map[column] = default_name
        
        if missing:
            raise ValueError(f"Missing items: {missing}.")
        
        return df.rename(columns = rename_map)
        