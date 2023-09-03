from python_keycloak_client.aio.mixins import WellKnownMixin
from python_keycloak_client.uma import PATH_WELL_KNOWN
from python_keycloak_client.uma import KeycloakUMA as SyncKeycloakUMA

__all__ = ("KeycloakUMA",)


class KeycloakUMA(WellKnownMixin, SyncKeycloakUMA):
    def get_path_well_known(self):
        return PATH_WELL_KNOWN
