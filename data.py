CONSTANTE_GRAVITACIONAL=6.672*10**-11
AU = 1.49597871*10**11
DATA = {
    "tierra":{
        "masa":5.972*10**24,#kg
        "radio":6375*10**3,#metros
        "sunDistancia":1.49597871*10**11,#1.496*10**11,#metros,
        "periodo": 365.26,#en dias usado unicamente para el ejer3
        #en el ejercio 4, usamos la formula 
        #para encontrar el periodo en segundos
    },
    "marte":{
        "masa":6.39*10**23,
        "radio":3389.5*10**3,
        "sunDistancia":2.2794*10**11,
        "periodo": 686.98,
    },
    "mercurio":{
        "masa":0.33010*10**24,
        "radio":2439.7*10**3,
        "sunDistancia":0.38*AU,
        "periodo": 87.97,
    },
    "venus":{
        "masa":4.867*10**24,
        "radio":6051.8*10**3,
        "sunDistancia":0.72*AU,
        "periodo": 224.70,
    },
    "jupiter":{#24.79
        "masa":1.898*10**27,
        "radio":69911*10**3,
        "sunDistancia":5.2*AU,
        "periodo": 4332.71,
    },
    "saturno":{#10.44
        "masa":5.683*10**26,
        "radio":58232*10**3,
        "sunDistancia":9.5*AU,
        "periodo": 10759.50,
    },
    "urano":{
        "masa":8.681*10**25,
        "radio":25362*10**3,
        "sunDistancia":2870972200*10**3,#19.8*AU,
        "periodo": 30685.00,
    },
    "neptuno":{
        "masa":1.024*10**26,
        "radio":24622*10**3,
        "sunDistancia":30*AU,
        "periodo": 60190.00,
    },
}