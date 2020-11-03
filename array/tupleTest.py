lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)

*head, b, c, d = range(5)
print(head) #[0, 1]
a, *body, b, c = range(5)
print(body) #[1, 2]
a, b, c, *rest = range(5)
print(rest) #[3, 4]

