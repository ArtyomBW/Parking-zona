mig:
	python3 manage.py makemigrations	# Migaratsiyani yaratish
	python3 manage.py migrate			# Migratsiya qilish

admin:
	python3 manage.py createsuperuser # Superadmin

apps:
	python3 manage.py startapp apps # Yangi apps papkasini yaratish

delete:
	find apps/migrations -type f -not -name '__init__.py' -delete  # init.py dan boshqasini o‘chirish

deleted:
	rm -f db.sqlite3 # Ma'lumotlar bazasini o'chirish

kesh:
	find /home/artyom/PycharmProjects/Exam_6/ -name "__pycache__" -exec rm -rf {} + # Bu ceshni tozalash uchun

unfold:
	pip install django-unfold # Django unfold admin panel

check-unfold:
	pip show django-unfold # Django unfold tekshirish

binary:
	pip install psycopg2-binary # Binary o'rnatish

reset:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete # init.py dan boshqasini o‘chirish
	find . -path "*/migrations/*.pyc" -delete
	psql -d db_100k -c "TRUNCATE TABLE django_migrations RESTART IDENTITY CASCADE;"
	python manage.py makemigrations
	python manage.py migrate

container:
	docker ps -a # Barcha ochiq yopiq containerlarni korish

shell:
	python manage.py dbshell # Django databasega ulanishini tekshirish

postgres:
	sudo systemctl status postgresql # postgres ishlayotganini tekshirish

S:
	docker start 817a25d83439 		 # Shaxsiy containerni aktivatsiya qilish

redis:
	docker start 4997e1a4e3eb # Redisni aktivatsiya qilish

Stub:
	pip3 install django-stubs # Objects funksiyasi uchun :)

Fix_product:
	python manage.py dumpdata apps.Product --indent 4 > product.json # Product uchun JSON fayl

Fix_up:
	make product-json # Json activate cod

Fix_category:
	python manage.py dumpdata apps.Category --indent 4 > category.json # Category uchun JSON fayl yaratish

Fix_cat:
	 python manage loaddata category.json # Category json fayl ni aktivatsiya qilish

push:
	@read -p "Commit izohini kiriting: " m; \
	git add . ; \
	git commit -m "$$m"; \
	git push

# Salmlar


