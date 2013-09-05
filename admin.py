import datetime

from flask_peewee.admin import Admin, ModelAdmin, AdminPanel

from app import app
from auth import auth
from models import User, Relationship


class UserStatsPanel(AdminPanel):
    template_name = 'admin/user_stats.html'

    def get_context(self):
        last_week = datetime.datetime.now() - datetime.timedelta(days=7)
        signups_this_week = User.select().where(User.joined > last_week).count()
        return {
            'signups': signups_this_week,
        }

class UserAdmin(ModelAdmin):
    # it doesn't work yet because flask-peewe has error
    columns = ('email', 'active', 'admin', 'joined')


admin = Admin(app, auth, branding=app.config['BRAND'])
auth.register_admin(admin, UserAdmin)

admin.register_panel('User stats', UserStatsPanel)

admin.register(Relationship)
