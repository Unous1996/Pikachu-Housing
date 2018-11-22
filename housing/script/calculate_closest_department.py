from os import sys, path
import django


def calculate_closest_deptid(house_id):
    from distance.models import Distance
    distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[house_id])
    for item in distance_set:
        return_id = item.department_id.id
        return float(return_id)
    return -1.0

if __name__ == "__main__":
	sys.path.append('/Users/tim/Desktop/CS411/Code/Pikachu-Housing')
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
	django.setup()
	from housing.models import House
	all_houses = House.objects.all()
	test_house = House.objects.first()
	print("test_house_id = %d", test_house_id)
	closest_dept_id = calculate_closest_deptid(house_id=test_house.id)
	test_house.closest_department_float