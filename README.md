historque azure terminal : 
Demande d'une instance Cloud Shell.Succeeded. 
Connecting terminal...

Subscription used to launch your CloudShell 7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc is not registered to Microsoft.CloudShell Namespace. Please follow these instructions "https://aka.ms/RegisterCloudShell" to register. In future, unregistered subscriptions will have restricted access to CloudShell service.

Your Cloud Shell session will be ephemeral so no files or system changes will persist beyond your current session.
abakhouch [ ~ ]$ ^[[200~(MissingSubscriptionRegistration) The subscription is not registered to use namespace 'Microsoft.ContainerService'. See https://aka.ms/rps-not-found for how to register subscriptions.
bash: syntax error near unexpected token `MissingSubscriptionRegistration'
abakhouch [ ~ ]$ Code: MissingSubscriptionRegistration
bash: Code:: command not found
abakhouch [ ~ ]$ Message: The subscription is not registered to use namespace 'Microsoft.ContainerService'. See https://aka.ms/rps-not-found for how to register subscriptions.
bash: Message:: command not found
abakhouch [ ~ ]$ Exception Details:      (MissingSubscriptionRegistration) The subscription is not registered to use namespace 'Microsoft.ContainerService'. See https://aka.ms/rps-not-found for how to register subscriptions.
bash: syntax error near unexpected token `('
abakhouch [ ~ ]$         Code: MissingSubscriptionRegistration
bash: Code:: command not found
abakhouch [ ~ ]$         Message: The subscription is not registered to use namespace 'Microsoft.ContainerService'. See https://aka.ms/rps-not-found for how to register subscriptions.
bash: Message:: command not found
abakhouch [ ~ ]$         Target: Microsoft.ContainerService~
bash: Target:: command not found
abakhouch [ ~ ]$ az provider show --namespace Microsoft.ContainerService --query "registrationState"

"NotRegistered"
abakhouch [ ~ ]$ 
abakhouch [ ~ ]$ 
abakhouch [ ~ ]$ az provider register --namespace Microsoft.ContainerService
Registering is still on-going. You can monitor using 'az provider show -n Microsoft.ContainerService'
abakhouch [ ~ ]$ az provider show --namespace Microsoft.ContainerService --query "registrationState"
"Registering"
abakhouch [ ~ ]$ az provider show --namespace Microsoft.ContainerService --query "registrationState"
"Registered"
abakhouch [ ~ ]$ az aks create \
  --resource-group mon-groupe-rg \
  --name mon-cluster-aks \
  --node-count 2 \
  --enable-addons monitoring \
  --generate-ssh-keys \
  --attach-acr monacr123
AAD role propagation done[############################################]  100.0000%{
  "aadProfile": null,
  "addonProfiles": {
    "omsagent": {
      "config": {
        "logAnalyticsWorkspaceResourceID": "/subscriptions/7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc/resourceGroups/DefaultResourceGroup-WEU/providers/Microsoft.OperationalInsights/workspaces/DefaultWorkspace-7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc-WEU",
        "useAADAuth": "true"
      },
      "enabled": true,
      "identity": null
    }
  },
  "agentPoolProfiles": [
    {
      "availabilityZones": null,
      "capacityReservationGroupId": null,
      "count": 2,
      "creationData": null,
      "currentOrchestratorVersion": "1.30.10",
      "eTag": null,
      "enableAutoScaling": false,
      "enableEncryptionAtHost": false,
      "enableFips": false,
      "enableNodePublicIp": false,
      "enableUltraSsd": false,
      "gpuInstanceProfile": null,
      "hostGroupId": null,
      "kubeletConfig": null,
      "kubeletDiskType": "OS",
      "linuxOsConfig": null,
      "maxCount": null,
      "maxPods": 250,
      "messageOfTheDay": null,
      "minCount": null,
      "mode": "System",
      "name": "nodepool1",
      "networkProfile": null,
      "nodeImageVersion": "AKSUbuntu-2204gen2containerd-202503.21.0",
      "nodeLabels": null,
      "nodePublicIpPrefixId": null,
      "nodeTaints": null,
      "orchestratorVersion": "1.30",
      "osDiskSizeGb": 128,
      "osDiskType": "Managed",
      "osSku": "Ubuntu",
      "osType": "Linux",
      "podSubnetId": null,
      "powerState": {
        "code": "Running"
      },
      "provisioningState": "Succeeded",
      "proximityPlacementGroupId": null,
      "scaleDownMode": "Delete",
      "scaleSetEvictionPolicy": null,
      "scaleSetPriority": null,
      "securityProfile": {
        "enableSecureBoot": false,
        "enableVtpm": false
      },
      "spotMaxPrice": null,
      "tags": null,
      "type": "VirtualMachineScaleSets",
      "upgradeSettings": {
        "drainTimeoutInMinutes": null,
        "maxSurge": "10%",
        "nodeSoakDurationInMinutes": null
      },
      "vmSize": "Standard_DS2_v2",
      "vnetSubnetId": null,
      "windowsProfile": null,
      "workloadRuntime": null
    }
  ],
  "apiServerAccessProfile": null,
  "autoScalerProfile": null,
  "autoUpgradeProfile": {
    "nodeOsUpgradeChannel": "NodeImage",
    "upgradeChannel": null
  },
  "azureMonitorProfile": {
    "metrics": null
  },
  "azurePortalFqdn": "mon-cluste-mon-groupe-rg-7abdfa-ton9frr0.portal.hcp.westeurope.azmk8s.io",
  "currentKubernetesVersion": "1.30.10",
  "disableLocalAccounts": false,
  "diskEncryptionSetId": null,
  "dnsPrefix": "mon-cluste-mon-groupe-rg-7abdfa",
  "eTag": null,
  "enablePodSecurityPolicy": null,
  "enableRbac": true,
  "extendedLocation": null,
  "fqdn": "mon-cluste-mon-groupe-rg-7abdfa-ton9frr0.hcp.westeurope.azmk8s.io",
  "fqdnSubdomain": null,
  "httpProxyConfig": null,
  "id": "/subscriptions/7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc/resourcegroups/mon-groupe-rg/providers/Microsoft.ContainerService/managedClusters/mon-cluster-aks",
  "identity": {
    "delegatedResources": null,
    "principalId": "c95d9db8-ffca-4905-9ab6-4f67b3415f8a",
    "tenantId": "509c723e-e2a6-4bff-a496-9cfed31354ed",
    "type": "SystemAssigned",
    "userAssignedIdentities": null
  },
  "identityProfile": {
    "kubeletidentity": {
      "clientId": "32fb12ae-7742-47b4-9cb5-2d9b681383bd",
      "objectId": "4e9efd7e-75c7-4c56-8d99-396a8f7e0021",
      "resourceId": "/subscriptions/7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc/resourcegroups/MC_mon-groupe-rg_mon-cluster-aks_westeurope/providers/Microsoft.ManagedIdentity/userAssignedIdentities/mon-cluster-aks-agentpool"
    }
  },
  "ingressProfile": null,
  "kubernetesVersion": "1.30",
  "linuxProfile": {
    "adminUsername": "azureuser",
    "ssh": {
      "publicKeys": [
        {
          "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCg0y4ficd4jfRD5ydcqJZF68cuaoLw2JzCzj+nds7JOOrd/66sC9ZDR1eV88hlq3R9GTb+Izd17Dh7EOqgPstbeQiY1H6bxvJYIthHNhmpIhKSb7BfbxvQCu6hPnZcRK7Y+zd8mDGre5ocd6lrm7+Nm7lrr5ICxh8dyiz2sHSnmhMmpmi5vVnfjXxS65jAOJb35OCto8VNz3G1qtnUSnLmydhgREnmP6YnBK4j4Kj0FGHIMBVPipDVX7FEy6647rWtI1sJb44UHn+pundl3Sbi5LkOTL79RPPomRRH/aPOPJYg4T+Ntw4L64qW2rNUrdlKwzp1pBCVKhUDGJBQTi4F"
        }
      ]
    }
  },
  "location": "westeurope",
  "maxAgentPools": 100,
  "metricsProfile": {
    "costAnalysis": {
      "enabled": false
    }
  },
  "name": "mon-cluster-aks",
  "networkProfile": {
    "advancedNetworking": null,
    "dnsServiceIp": "10.0.0.10",
    "ipFamilies": [
      "IPv4"
    ],
    "loadBalancerProfile": {
      "allocatedOutboundPorts": null,
      "backendPoolType": "nodeIPConfiguration",
      "effectiveOutboundIPs": [
        {
          "id": "/subscriptions/7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc/resourceGroups/MC_mon-groupe-rg_mon-cluster-aks_westeurope/providers/Microsoft.Network/publicIPAddresses/6812baab-6c6a-4f29-b6b1-105ea26439f4",
          "resourceGroup": "MC_mon-groupe-rg_mon-cluster-aks_westeurope"
        }
      ],
      "enableMultipleStandardLoadBalancers": null,
      "idleTimeoutInMinutes": null,
      "managedOutboundIPs": {
        "count": 1,
        "countIpv6": null
      },
      "outboundIPs": null,
      "outboundIpPrefixes": null
    },
    "loadBalancerSku": "standard",
    "natGatewayProfile": null,
    "networkDataplane": "azure",
    "networkMode": null,
    "networkPlugin": "azure",
    "networkPluginMode": "overlay",
    "networkPolicy": "none",
    "outboundType": "loadBalancer",
    "podCidr": "10.244.0.0/16",
    "podCidrs": [
      "10.244.0.0/16"
    ],
    "serviceCidr": "10.0.0.0/16",
    "serviceCidrs": [
      "10.0.0.0/16"
    ]
  },
  "nodeResourceGroup": "MC_mon-groupe-rg_mon-cluster-aks_westeurope",
  "nodeResourceGroupProfile": null,
  "oidcIssuerProfile": {
    "enabled": false,
    "issuerUrl": null
  },
  "podIdentityProfile": null,
  "powerState": {
    "code": "Running"
  },
  "privateFqdn": null,
  "privateLinkResources": null,
  "provisioningState": "Succeeded",
  "publicNetworkAccess": null,
  "resourceGroup": "mon-groupe-rg",
  "resourceUid": "67f672ff8fe4610001a54023",
  "securityProfile": {
    "azureKeyVaultKms": null,
    "defender": null,
    "imageCleaner": null,
    "workloadIdentity": null
  },
  "serviceMeshProfile": null,
  "servicePrincipalProfile": {
    "clientId": "msi",
    "secret": null
  },
  "sku": {
    "name": "Base",
    "tier": "Free"
  },
  "storageProfile": {
    "blobCsiDriver": null,
    "diskCsiDriver": {
      "enabled": true
    },
    "fileCsiDriver": {
      "enabled": true
    },
    "snapshotController": {
      "enabled": true
    }
  },
  "supportPlan": "KubernetesOfficial",
  "systemData": null,
  "tags": null,
  "type": "Microsoft.ContainerService/ManagedClusters",
  "upgradeSettings": null,
  "windowsProfile": null,
  "workloadAutoScalerProfile": {
    "keda": null,
    "verticalPodAutoscaler": null
  }
}
abakhouch [ ~ ]$ az aks get-credentials --resource-group mon-groupe-rg --name mon-cluster-aks 
Merged "mon-cluster-aks" as current context in /home/abakhouch/.kube/config
abakhouch [ ~ ]$ kubectl apply -f configmap.yml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
error: the path "configmap.yml" does not exist
error: the path "deployment.yml" does not exist
error: the path "service.yml" does not exist
abakhouch [ ~ ]$ ^[[200~nano configmap.yml
bash: $'\E[200~nano': command not found
abakhouch [ ~ ]$ kubectl apply -f configmap.yml
configmap/flask-config created
abakhouch [ ~ ]$ kubectl apply -f service.yml
service/flask-service created
abakhouch [ ~ ]$ kubectl apply -f deployment.yml
deployment.apps/flask-deployment created
abakhouch [ ~ ]$ ls
configmap.yml  deployment.yml  service.yml
abakhouch [ ~ ]$ ^[[200~kubectl apply -f configmap.yml
bash: $'\E[200~kubectl': command not found
abakhouch [ ~ ]$ kubectl apply -f deployment.yml
deployment.apps/flask-deployment unchanged
abakhouch [ ~ ]$ kubectl apply -f service.yml
service/flask-service unchanged
abakhouch [ ~ ]$ ~kubectl apply -f configmap.yml
kubectl apply -f deployment.yml
kubectl apply -f service.yml
bash: ~kubectl: command not found
deployment.apps/flask-deployment unchanged
service/flask-service unchanged
abakhouch [ ~ ]$ kubectl get pods
NAME                                READY   STATUS         RESTARTS   AGE
flask-deployment-7b4d6f586b-42mwv   0/1     ErrImagePull   0          109s
flask-deployment-7b4d6f586b-pqb7k   0/1     ErrImagePull   0          109s
abakhouch [ ~ ]$ kubectl get svc
NAME            TYPE           CLUSTER-IP    EXTERNAL-IP       PORT(S)        AGE
flask-service   LoadBalancer   10.0.39.247   132.220.105.103   80:30678/TCP   2m15s
kubernetes      ClusterIP      10.0.0.1      <none>            443/TCP        9m55s
abakhouch [ ~ ]$ kubectl get svc
NAME            TYPE           CLUSTER-IP    EXTERNAL-IP       PORT(S)        AGE
flask-service   LoadBalancer   10.0.39.247   132.220.105.103   80:30678/TCP   2m24s
kubernetes      ClusterIP      10.0.0.1      <none>            443/TCP        10m
abakhouch [ ~ ]$ kubectl get pods
NAME                                READY   STATUS             RESTARTS   AGE
flask-deployment-7b4d6f586b-42mwv   0/1     ImagePullBackOff   0          4m10s
flask-deployment-7b4d6f586b-pqb7k   0/1     ImagePullBackOff   0          4m10s
abakhouch [ ~ ]$ kubectl describe pod flask-deployment-7b4d6f586b-42mwv
Name:             flask-deployment-7b4d6f586b-42mwv
Namespace:        default
Priority:         0
Service Account:  default
Node:             aks-nodepool1-27672355-vmss000000/10.224.0.4
Start Time:       Wed, 09 Apr 2025 13:25:17 +0000
Labels:           app=flask
                  pod-template-hash=7b4d6f586b
Annotations:      <none>
Status:           Pending
IP:               10.244.0.228
IPs:
  IP:           10.244.0.228
Controlled By:  ReplicaSet/flask-deployment-7b4d6f586b
Containers:
  flask-container:
    Container ID:   
    Image:          monacr123.azurecr.io/flask-app:latest
    Image ID:       
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:
      STORAGE_PATH:  <set to the key 'blob_url' of config map 'flask-config'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zhsg4 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-zhsg4:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                    From               Message
  ----     ------     ----                   ----               -------
  Normal   Scheduled  5m29s                  default-scheduler  Successfully assigned default/flask-deployment-7b4d6f586b-42mwv to aks-nodepool1-27672355-vmss000000
  Normal   Pulling    4m (x4 over 5m29s)     kubelet            Pulling image "monacr123.azurecr.io/flask-app:latest"
  Warning  Failed     4m (x4 over 5m28s)     kubelet            Failed to pull image "monacr123.azurecr.io/flask-app:latest": [rpc error: code = NotFound desc = failed to pull and unpack image "monacr123.azurecr.io/flask-app:latest": failed to resolve reference "monacr123.azurecr.io/flask-app:latest": monacr123.azurecr.io/flask-app:latest: not found, failed to pull and unpack image "monacr123.azurecr.io/flask-app:latest": failed to resolve reference "monacr123.azurecr.io/flask-app:latest": failed to authorize: failed to fetch anonymous token: unexpected status from GET request to https://monacr123.azurecr.io/oauth2/token?scope=repository%3Aflask-app%3Apull&service=monacr123.azurecr.io: 401 Unauthorized]
  Warning  Failed     4m (x4 over 5m28s)     kubelet            Error: ErrImagePull
  Warning  Failed     3m46s (x6 over 5m27s)  kubelet            Error: ImagePullBackOff
  Normal   BackOff    22s (x21 over 5m27s)   kubelet            Back-off pulling image "monacr123.azurecr.io/flask-app:latest"
abakhouch [ ~ ]$ az acr credential show --name monacr123
Run 'az acr update -n monacr123 --admin-enabled true' to enable admin first.
abakhouch [ ~ ]$ az acr update -n monacr123 --admin-enabled true
{
  "adminUserEnabled": true,
  "anonymousPullEnabled": false,
  "creationDate": "2025-04-09T12:54:31.323568+00:00",
  "dataEndpointEnabled": false,
  "dataEndpointHostNames": [],
  "encryption": {
    "keyVaultProperties": null,
    "status": "disabled"
  },
  "id": "/subscriptions/7abdfa03-e0ac-4bf1-b7e4-ddfd727aeedc/resourceGroups/mon-groupe-rg/providers/Microsoft.ContainerRegistry/registries/monacr123",
  "identity": null,
  "location": "westeurope",
  "loginServer": "monacr123.azurecr.io",
  "metadataSearch": "Disabled",
  "name": "monacr123",
  "networkRuleBypassOptions": "AzureServices",
  "networkRuleSet": null,
  "policies": {
    "azureAdAuthenticationAsArmPolicy": {
      "status": "enabled"
    },
    "exportPolicy": {
      "status": "enabled"
    },
    "quarantinePolicy": {
      "status": "disabled"
    },
    "retentionPolicy": {
      "days": 7,
      "lastUpdatedTime": "2025-04-09T12:54:39.938728+00:00",
      "status": "disabled"
    },
    "softDeletePolicy": {
      "lastUpdatedTime": "2025-04-09T12:54:39.938764+00:00",
      "retentionDays": 7,
      "status": "disabled"
    },
    "trustPolicy": {
      "status": "disabled",
      "type": "Notary"
    }
  },
  "privateEndpointConnections": [],
  "provisioningState": "Succeeded",
  "publicNetworkAccess": "Enabled",
  "resourceGroup": "mon-groupe-rg",
  "sku": {
    "name": "Basic",
    "tier": "Basic"
  },
  "status": null,
  "systemData": {
    "createdAt": "2025-04-09T12:54:31.323568+00:00",
    "createdBy": "fabakhouch.ir2025@esaip.org",
    "createdByType": "User",
    "lastModifiedAt": "2025-04-09T13:31:43.663584+00:00",
    "lastModifiedBy": "fabakhouch.ir2025@esaip.org",
    "lastModifiedByType": "User"
  },
  "tags": {},
  "type": "Microsoft.ContainerRegistry/registries",
  "zoneRedundancy": "Disabled"
}
abakhouch [ ~ ]$ az acr credential show --name monacr123
[Warning] This output may compromise security by showing the following secrets: passwords, value. Learn more at: https://go.microsoft.com/fwlink/?linkid=2258669
{
  "passwords": [
    {
      "name": "password",
      "value": "tHiaGWtlW9B9N3SuhFrpy6pAbKSn+Umfxun7emdc4m+ACRAuV43l"
    },
    {
      "name": "password2",
      "value": "XrtN+iz4BeQu+M5UxM62KdTy2kp1lbhCVTtOXuWbg2+ACRDWfIud"
    }
  ],
  "username": "monacr123"
}
abakhouch [ ~ ]$ kubectl create secret docker-registry acr-secret \
  --docker-server=monacr123.azurecr.io \
  --docker-username=monacr123 \
  --docker-password="tHiaGWtlW9B9N3SuhFrpy6pAbKSn+Umfxun7emdc4m+ACRAuV43l" \
  --docker-email=teplitxkymatthis@gmail.com
secret/acr-secret created
abakhouch [ ~ ]$ kubectl apply -f deployment.yml
deployment.apps/flask-deployment configured
abakhouch [ ~ ]$ kubectl get pods
NAME                                READY   STATUS             RESTARTS   AGE
flask-deployment-799b8cbbbf-vm4f8   0/1     ErrImagePull       0          7s
flask-deployment-7b4d6f586b-pqb7k   0/1     ImagePullBackOff   0          8m17s
abakhouch [ ~ ]$ az acr repository list --name monacr123 --output table

abakhouch [ ~ ]$ az acr repository list --name monacr123 --output table

abakhouch [ ~ ]$ ^C
