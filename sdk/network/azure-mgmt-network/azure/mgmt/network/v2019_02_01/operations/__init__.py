# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import ApplicationGatewaysOperations
from ._operations import ApplicationSecurityGroupsOperations
from ._operations import AvailableDelegationsOperations
from ._operations import AvailableResourceGroupDelegationsOperations
from ._operations import AzureFirewallsOperations
from ._operations import AzureFirewallFqdnTagsOperations
from ._operations import NetworkManagementClientOperationsMixin
from ._operations import DdosCustomPoliciesOperations
from ._operations import DdosProtectionPlansOperations
from ._operations import AvailableEndpointServicesOperations
from ._operations import ExpressRouteCircuitAuthorizationsOperations
from ._operations import ExpressRouteCircuitPeeringsOperations
from ._operations import ExpressRouteCircuitConnectionsOperations
from ._operations import PeerExpressRouteCircuitConnectionsOperations
from ._operations import ExpressRouteCircuitsOperations
from ._operations import ExpressRouteServiceProvidersOperations
from ._operations import ExpressRouteCrossConnectionsOperations
from ._operations import ExpressRouteCrossConnectionPeeringsOperations
from ._operations import ExpressRouteGatewaysOperations
from ._operations import ExpressRouteConnectionsOperations
from ._operations import ExpressRoutePortsLocationsOperations
from ._operations import ExpressRoutePortsOperations
from ._operations import ExpressRouteLinksOperations
from ._operations import InterfaceEndpointsOperations
from ._operations import LoadBalancersOperations
from ._operations import LoadBalancerBackendAddressPoolsOperations
from ._operations import LoadBalancerFrontendIPConfigurationsOperations
from ._operations import InboundNatRulesOperations
from ._operations import LoadBalancerLoadBalancingRulesOperations
from ._operations import LoadBalancerOutboundRulesOperations
from ._operations import LoadBalancerNetworkInterfacesOperations
from ._operations import LoadBalancerProbesOperations
from ._operations import NatGatewaysOperations
from ._operations import NetworkInterfacesOperations
from ._operations import NetworkInterfaceIPConfigurationsOperations
from ._operations import NetworkInterfaceLoadBalancersOperations
from ._operations import NetworkInterfaceTapConfigurationsOperations
from ._operations import NetworkProfilesOperations
from ._operations import NetworkSecurityGroupsOperations
from ._operations import SecurityRulesOperations
from ._operations import DefaultSecurityRulesOperations
from ._operations import NetworkWatchersOperations
from ._operations import PacketCapturesOperations
from ._operations import ConnectionMonitorsOperations
from ._operations import Operations
from ._operations import PublicIPAddressesOperations
from ._operations import PublicIPPrefixesOperations
from ._operations import RouteFiltersOperations
from ._operations import RouteFilterRulesOperations
from ._operations import RouteTablesOperations
from ._operations import RoutesOperations
from ._operations import BgpServiceCommunitiesOperations
from ._operations import ServiceEndpointPoliciesOperations
from ._operations import ServiceEndpointPolicyDefinitionsOperations
from ._operations import UsagesOperations
from ._operations import VirtualNetworksOperations
from ._operations import SubnetsOperations
from ._operations import ResourceNavigationLinksOperations
from ._operations import ServiceAssociationLinksOperations
from ._operations import VirtualNetworkPeeringsOperations
from ._operations import VirtualNetworkGatewaysOperations
from ._operations import VirtualNetworkGatewayConnectionsOperations
from ._operations import LocalNetworkGatewaysOperations
from ._operations import VirtualNetworkTapsOperations
from ._operations import VirtualWansOperations
from ._operations import VpnSitesOperations
from ._operations import VpnSitesConfigurationOperations
from ._operations import VirtualHubsOperations
from ._operations import HubVirtualNetworkConnectionsOperations
from ._operations import VpnGatewaysOperations
from ._operations import VpnConnectionsOperations
from ._operations import P2SVpnServerConfigurationsOperations
from ._operations import P2SVpnGatewaysOperations
from ._operations import WebApplicationFirewallPoliciesOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApplicationGatewaysOperations",
    "ApplicationSecurityGroupsOperations",
    "AvailableDelegationsOperations",
    "AvailableResourceGroupDelegationsOperations",
    "AzureFirewallsOperations",
    "AzureFirewallFqdnTagsOperations",
    "NetworkManagementClientOperationsMixin",
    "DdosCustomPoliciesOperations",
    "DdosProtectionPlansOperations",
    "AvailableEndpointServicesOperations",
    "ExpressRouteCircuitAuthorizationsOperations",
    "ExpressRouteCircuitPeeringsOperations",
    "ExpressRouteCircuitConnectionsOperations",
    "PeerExpressRouteCircuitConnectionsOperations",
    "ExpressRouteCircuitsOperations",
    "ExpressRouteServiceProvidersOperations",
    "ExpressRouteCrossConnectionsOperations",
    "ExpressRouteCrossConnectionPeeringsOperations",
    "ExpressRouteGatewaysOperations",
    "ExpressRouteConnectionsOperations",
    "ExpressRoutePortsLocationsOperations",
    "ExpressRoutePortsOperations",
    "ExpressRouteLinksOperations",
    "InterfaceEndpointsOperations",
    "LoadBalancersOperations",
    "LoadBalancerBackendAddressPoolsOperations",
    "LoadBalancerFrontendIPConfigurationsOperations",
    "InboundNatRulesOperations",
    "LoadBalancerLoadBalancingRulesOperations",
    "LoadBalancerOutboundRulesOperations",
    "LoadBalancerNetworkInterfacesOperations",
    "LoadBalancerProbesOperations",
    "NatGatewaysOperations",
    "NetworkInterfacesOperations",
    "NetworkInterfaceIPConfigurationsOperations",
    "NetworkInterfaceLoadBalancersOperations",
    "NetworkInterfaceTapConfigurationsOperations",
    "NetworkProfilesOperations",
    "NetworkSecurityGroupsOperations",
    "SecurityRulesOperations",
    "DefaultSecurityRulesOperations",
    "NetworkWatchersOperations",
    "PacketCapturesOperations",
    "ConnectionMonitorsOperations",
    "Operations",
    "PublicIPAddressesOperations",
    "PublicIPPrefixesOperations",
    "RouteFiltersOperations",
    "RouteFilterRulesOperations",
    "RouteTablesOperations",
    "RoutesOperations",
    "BgpServiceCommunitiesOperations",
    "ServiceEndpointPoliciesOperations",
    "ServiceEndpointPolicyDefinitionsOperations",
    "UsagesOperations",
    "VirtualNetworksOperations",
    "SubnetsOperations",
    "ResourceNavigationLinksOperations",
    "ServiceAssociationLinksOperations",
    "VirtualNetworkPeeringsOperations",
    "VirtualNetworkGatewaysOperations",
    "VirtualNetworkGatewayConnectionsOperations",
    "LocalNetworkGatewaysOperations",
    "VirtualNetworkTapsOperations",
    "VirtualWansOperations",
    "VpnSitesOperations",
    "VpnSitesConfigurationOperations",
    "VirtualHubsOperations",
    "HubVirtualNetworkConnectionsOperations",
    "VpnGatewaysOperations",
    "VpnConnectionsOperations",
    "P2SVpnServerConfigurationsOperations",
    "P2SVpnGatewaysOperations",
    "WebApplicationFirewallPoliciesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
