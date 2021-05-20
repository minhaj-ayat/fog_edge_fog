from oidc_provider.lib.claims import ScopeClaims
from django.utils.translation import ugettext as _


def userinfo(claims, user):
    claims['name'] = '{0} {1}'.format(user.first_name, user.last_name)
    claims['given_name'] = user.first_name
    claims['family_name'] = user.last_name
    claims['email'] = user.email

    return claims


class CustomScopeClaims(ScopeClaims):
    info_foo = (
        _(u'Foo'),
        _(u'Some description for the scope.'),
    )

    def scope_foo(self):
        # self.user - Django user instance.
        # self.userinfo - Dict returned by OIDC_USERINFO function.
        # self.scopes - List of scopes requested.
        # self.client - Client requesting this claims.
        dic = {
             'autn': "225b5ce8b199b49faa5f0a2ee238a6uy",
             'rand': "23553cbe9637a89d218ae64dae47bf35",
           #  'autn': autn,
            # 'rand': rand
        }

        return dic

    # If you want to change the description of the profile scope, you can redefine it.
    '''info_profile = (
        _(u'Profile'),
        _(u'Another description.'),
    )'''
