from polyUnit import polyUnit
def Translate (sPolynomial="1x^2+3x^3+x^2"):
    translatedPoly=[];

    hWords= sPolynomial.split("+");

    for i in range(0,len(hWords)):
        splitWord= hWords[i].split("^");
        if(len(splitWord)==1):
            hExponent=0;
        else:
            hExponent=splitWord[1];

        hFactor=splitWord[0].replace("x","");
        #incase theres "default" 1 before x ex: x^3, x^1 not 2x^3, 1x^1
        if len(hFactor)==0:
            hFactor=1;

        translatedPoly.append(polyUnit(hExponent, hFactor));

    return translatedPoly;
