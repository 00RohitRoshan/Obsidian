# Stage Redirect
|gateway name|Service name|Project|Cluster|nameSpace|Branch|
|--|--|--|--|--|--|
|Unified stage|whitelabel-stage-gateway|isu-internal|kubernetes-uat-cluster| |unified-redirect-stage|
|Unified onprem stage|redirect[gateway ns]|on-premise|on-premise| |unified-redirect-stage|
|SDK stage gateway|sdk-redirect|isu-internal|kubernetes-uat-cluster| |sdk-redirect-deployed|
|SDK new stage Gateway|sdk-redirect|isu-internal|kubernetes-uat-cluster| |sdk-redirect-deployed|
|Services Stage|istio-ingressgateway|isu-internal|kubernetes-uat-cluster| |[🤔Doubt]|
|onprem services stage|istio-ingressgateway, port=80|on-premise|on-premise| |[🤔Doubt]|
|Cbs stage|istio-ingressgateway|isu-internal|kubernetes-uat-cluster| |cbsgw-stage|
|cbs onprem stage|redirect[gateway ns]|on-premise|on-premise| |cbsgw-stage|
|IPPB stage|ippb-stage-gateway-redirect|isu-internal|kubernetes-uat-cluster| |ippb-encr|
|Card switch stage|istio-ingressgateway|isu-switch-staging|card-stage-cluster| |card-stage-redirect [🤔Doubt]|
|Card switch stage services|istio-ingressgateway|isu-switch-staging|card-stage-cluster| |card-stage-redirect [🤔Doubt]|



# Auth Application
|gateway name|Service name|Project|Cluster|nameSpace|Branch|
|--|--|--|--|--|--|
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
|Unified Prod|iserveuauthgateway-unified|unified-redirect-prod|creditapp|kube-prod-cluster
Unified Prod|unified-gateway-auth|unifiedgateway_prod|creditapp|kube-prod-cluster|

||gateway name||Service name||Branch||Project||Cluster||nameSpace||
|Unified Prod|iserveuauthgateway-unified|unified-redirect-prod|creditapp|kube-prod-cluster|
