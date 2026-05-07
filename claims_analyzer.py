class ClaimsAnalyzer:
        def __init__(self):
                self.claims = {}
                self.total_amount = 0
        def add_claim(self, member_id, amount, denial_code):
                self.claims.setdefault(denial_code, []).append({'member_id': member_id, 'amount': amount})
                self.total_amount += amount

        def get_denied(self, denial_code):
                return self.claims.get(denial_code,[])
        def total_denied(self):
                total = 0
                for k,v in self.claims.items():
                    if k is not None:
                        for each in v:
                                total += each['amount']
                return total
        def summary(self):
                summary_dict = {}
                for k,v in self.claims.items():
                    if k is not None:
                        summary_dict[k] = len(v)
                return summary_dict
        
analyzer = ClaimsAnalyzer()
analyzer.add_claim("M001", 450.00, "CO-45")
analyzer.add_claim("M002", 1200.00, None)
analyzer.add_claim("M003", 89.50, "CO-45")
analyzer.add_claim("M004", 300.00, "PR-1")

print(analyzer.get_denied("CO-45"))
print(analyzer.total_denied())
print(analyzer.summary())
