from django.contrib.auth.models import User, check_password
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.db import connections
from django.contrib.auth import get_user_model

class MyBackend(ModelBackend):
	
	def authenticate(self, username, password):
		row = self._connect_to_oracle(username)
		user = self._find_existing_user(username, row[1])
		if user:
			UserModel = get_user_model()
			user = UserModel._default_manager.get_by_natural_key(username)
			if check_password(password, user.password):
				return user
		else:
			user = self._create_new_user_(row[0], row[1])
			return user

	def _connect_to_oracle(self, username):
		cursor = connections['creditinals'].cursor()
		row = cursor.execute("select username, password_hash from userbase where username = %s", 
			[username]).fetchone()
		if (row == None):
			return 'No such user'
		return list(row)

	def _find_existing_user(self, username, new_password):
		try:
			user = User.objects.get(username=username)
			user.set_password(new_password)
			user.save()
		except User.DoesNotExist:
			user = None
		if user:
			return user
		else:
			return None

	def _create_new_user_(self,username, password):
		user = User.objects.create_user(username)
		user.set_password(password)
		user.is_active = True
		user.save()
		return user	