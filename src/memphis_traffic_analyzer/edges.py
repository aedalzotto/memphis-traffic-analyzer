class Edges:
    def __init__(self, df):
        prods = list(set(df['prod'].tolist()))

        self.edges = {}

        for prod in prods:
            conss = list(set(df[df['prod'] == prod]['cons'].tolist()))
            for cons in conss:
                prod_df = df[df['prod'] == prod]
                edge_df = prod_df[prod_df['cons'] == cons]
                self.edges[(prod,cons)] = edge_df
                self.edges[(prod,cons)].reset_index(drop = True, inplace = True)

    def __len__(self):
        return len(self.edges)
    
    def __iter__(self):
        return iter(self.edges)

    def __getitem__(self, key):
        return self.edges[key]
