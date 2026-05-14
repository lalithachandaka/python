class ClaimsAnalyzer:
        def __init__(self):
                self.claims = {}
                self.total_amount = 0
        def add_claim(self, member_id, amount, denial_code):
                if not member_id:
                        print(f"Skipping claim: member_id is empty")
                        return
                
                try:
                        amount = float(amount)
                except (ValueError, TypeError):
                        print(f"Skipping claim: invalid amount '{amount}'")
                        return
                if amount <= 0:
                        print(f"Skipping claim: amount must be greater than zero")
                        return
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
analyzer.add_claim("", 450.00, "CO-45")
analyzer.add_claim("M005", "abc", "CO-45")  # invalid amount
analyzer.add_claim("M006", -100, "CO-45")   # negative amount
analyzer.add_claim("M007", 0, "CO-45")      # zero amount

print(analyzer.get_denied("CO-45"))
print(analyzer.total_denied())
print(analyzer.summary())
