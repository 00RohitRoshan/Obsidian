|gateway name|Service name|Project|Cluster|nameSpace|Branch|
|Unified stage|unified-gateway-auth| isu-internal |kubernetes-uat-cluster|default|unifiedgateway_stage |
|Unified onprem stage|ext-auth|on-premise|on-premise||card-acquiring|
|SDK stage gateway	        |sdk-auth 		              | isu-internal |kubernetes-uat-cluster|default|sdk-auth-stage|
|cbs onprem stage	        |ext-auth gateway ns ,port=80	              | on-premise |on-premise||card-acquiring|
|IPPB stage		                |ippb-stage-gateway-auth | isu-internal |kubernetes-uat-cluster|default|ippb-auth-gateway-stage|
|Card switch stage|card-auth-stage| isu-switch-staging |card-stage-cluster|gateway|card-stage|

## UAT
|gateway name|Service name|Branch|Project|Cluster|nameSpace|
--|--|--|--|--|--|
Unified UAT|


## Prod
|gateway name|Service name|Branch|Project|Cluster|nameSpace|
--|--|--|--|--|--|
Unified Prod|unified-gateway-auth|unifiedgateway_prod|creditapp|kube-prod-cluster|
