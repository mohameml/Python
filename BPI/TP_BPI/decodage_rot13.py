def decodage(texte):
    l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    

    chaine=""
    for i in texte :
        if i in l:
           chaine+=l[l.index(i)+13]
        else:
            chaine+=i
            
    return chaine
print(decodage("Ibvyn, yr ebg13 rfg qrpbqr. Fv ibhf rgrf znyvaf, ibhf nirm fnaf qbhgr erznedhr dhr yr jro ertbetr qr pbqrhe/qrpbqrhe ebg13 ra yvtar, qbap, ha oba zbgrhe qr erpurepur n yn znva, ba gebhir encvqrzrag fba obaurhe (rg p'rgnvg ovra yr ohg qr y'rkrepvpr !). Yrf Rznpfvraf nhebag cersrer Z-k ebg13-ertvba ERG, znvf p'rfg har nhger uvfgbver. Abhf abhf eraqbaf znvagranag fhe Punzvyb. Punzvyb rfg npprffvoyr qrchvf y'npphrvy qr y'vagenarg Rafvznt (uggcf://vagenarg.rafvznt.teraboyr-vac.se/). Nyyrm-l, rg gebhirm (pr a'rfg cnf snpvyr) yr pbhef Rafvznt « Rafvznt 3ZZHAVK Havk : vagebqhpgvba rg cebtenzzngvba furyy ». Bhierm y'bhgvy « Qbphzragf » : ibhf gebhirerm ha qbphzrag dhv rfg y'égncr N3 qh wrh qr cvfgr."))

        
