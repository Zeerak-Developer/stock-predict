from flask import Flask,jsonify
import pickle
import numpy as np
import os
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/predict61',methods=['GET'])
def predict61():
    pkl61_file=open('gphA.pkl', 'rb')
    mydict61 = pickle.load(pkl61_file)
    pkl61_file.close( )

    return jsonify({"Result61": mydict61})

@app.route('/predict',methods=['GET'])
def predict():
    pkl_file=open('apple1.pkl', 'rb')
    mydict=pickle.load(pkl_file)
    pkl_file.close( )

    return jsonify({"Result": mydict})

@app.route('/predict1',methods=['GET'])
def predict1():
    pkl1_file=open('apple2.pkl', 'rb')
    mydict1=pickle.load(pkl1_file)
    pkl1_file.close( )

    return jsonify({"Result1": mydict1})

@app.route('/predict62',methods=['GET'])
def predict62():
    pkl62_file=open('gphMsft.pkl', 'rb')
    mydict62=pickle.load(pkl62_file)
    pkl62_file.close( )

    return jsonify({"Result62": mydict62})

@app.route('/predict2',methods=['GET'])
def predict2():
    pkl2_file=open('Msft1.pkl', 'rb')
    mydict2=pickle.load(pkl2_file)
    pkl2_file.close( )

    return jsonify({"Result2": mydict2})

@app.route('/predict3',methods=['GET'])
def predict3():
    pkl3_file=open('Msft2.pkl', 'rb')
    mydict3=pickle.load(pkl3_file)
    pkl3_file.close( )

    return jsonify({"Result3": mydict3})

@app.route('/predict63',methods=['GET'])
def predict63():
    pkl63_file=open('gphIBM.pkl', 'rb')
    mydict63=pickle.load(pkl63_file)
    pkl63_file.close( )

    return jsonify({"Result63": mydict63})

@app.route('/predict4',methods=['GET'])
def predict4():
    pkl4_file=open('IBM1.pkl', 'rb')
    mydict4=pickle.load(pkl4_file)
    pkl4_file.close( )

    return jsonify({"Result4": mydict4})

@app.route('/predict5',methods=['GET'])
def predict5():
    pkl5_file=open('IBM2.pkl', 'rb')
    mydict5=pickle.load(pkl5_file)
    pkl5_file.close( )

    return jsonify({"Result5": mydict5})

@app.route('/predict64',methods=['GET'])
def predict64():
    pkl64_file=open('gphGO.pkl', 'rb')
    mydict64=pickle.load(pkl64_file)
    pkl64_file.close( )

    return jsonify({"Result64": mydict64})

@app.route('/predict6',methods=['GET'])
def predict6():
    pkl6_file=open('GOOGLE1.pkl', 'rb')
    mydict6=pickle.load(pkl6_file)
    pkl6_file.close( )

    return jsonify({"Result6": mydict6})

@app.route('/predict7',methods=['GET'])
def predict7():
    pkl7_file=open('GOOGLE2.pkl', 'rb')
    mydict7=pickle.load(pkl7_file)
    pkl7_file.close( )

    return jsonify({"Result7": mydict7})

@app.route('/predict65',methods=['GET'])
def predict65():
    pkl65_file=open('gphORCL.pkl', 'rb')
    mydict65=pickle.load(pkl65_file)
    pkl65_file.close( )

    return jsonify({"Result65": mydict65})

@app.route('/predict8',methods=['GET'])
def predict8():
    pkl8_file=open('ORACLE1.pkl', 'rb')
    mydict8=pickle.load(pkl8_file)
    pkl8_file.close( )

    return jsonify({"Result8": mydict8})

@app.route('/predict9',methods=['GET'])
def predict9():
    pkl9_file=open('ORACLE2.pkl', 'rb')
    mydict9=pickle.load(pkl9_file)
    pkl9_file.close( )

    return jsonify({"Result9": mydict9})

@app.route('/predict66',methods=['GET'])
def predict66():
    pkl66_file=open('gphMA.pkl', 'rb')
    mydict66=pickle.load(pkl66_file)
    pkl66_file.close( )

    return jsonify({"Result66": mydict66})

@app.route('/predict10',methods=['GET'])
def predict10():
    pkl10_file=open('Master1.pkl', 'rb')
    mydict10=pickle.load(pkl10_file)
    pkl10_file.close( )

    return jsonify({"Result10": mydict10})

@app.route('/predict11',methods=['GET'])
def predict11():
    pkl11_file=open('Master2.pkl', 'rb')
    mydict11=pickle.load(pkl11_file)
    pkl11_file.close( )

    return jsonify({"Result11": mydict11})

@app.route('/predict67',methods=['GET'])
def predict67():
    pkl67_file=open('gphBOA.pkl', 'rb')
    mydict67=pickle.load(pkl67_file)
    pkl67_file.close( )

    return jsonify({"Result67": mydict67})

@app.route('/predict12',methods=['GET'])
def predict12():
    pkl12_file=open('BOA1.pkl', 'rb')
    mydict12=pickle.load(pkl12_file)
    pkl12_file.close( )

    return jsonify({"Result12": mydict12})

@app.route('/predict13',methods=['GET'])
def predict13():
    pkl13_file=open('BOA2.pkl', 'rb')
    mydict13=pickle.load(pkl13_file)
    pkl13_file.close( )

    return jsonify({"Result13": mydict13})

@app.route('/predict68',methods=['GET'])
def predict68():
    pkl68_file=open('gphPay.pkl', 'rb')
    mydict68=pickle.load(pkl68_file)
    pkl68_file.close( )

    return jsonify({"Result68": mydict68})

@app.route('/predict14',methods=['GET'])
def predict14():
    pkl14_file=open('Paypal1.pkl', 'rb')
    mydict14=pickle.load(pkl14_file)
    pkl14_file.close( )

    return jsonify({"Result14": mydict14})

@app.route('/predict15',methods=['GET'])
def predict15():
    pkl15_file=open('Paypal2.pkl', 'rb')
    mydict15=pickle.load(pkl15_file)
    pkl15_file.close( )

    return jsonify({"Result15": mydict15})

@app.route('/predict69',methods=['GET'])
def predict69():
    pkl69_file=open('gphVisa.pkl', 'rb')
    mydict69=pickle.load(pkl69_file)
    pkl69_file.close( )

    return jsonify({"Result69": mydict69})

@app.route('/predict16',methods=['GET'])
def predict16():
    pkl16_file=open('Visa1.pkl', 'rb')
    mydict16=pickle.load(pkl16_file)
    pkl16_file.close( )

    return jsonify({"Result16": mydict16})

@app.route('/predict17',methods=['GET'])
def predict17():
    pkl17_file=open('Visa2.pkl', 'rb')
    mydict17=pickle.load(pkl17_file)
    pkl17_file.close( )

    return jsonify({"Result17": mydict17})

@app.route('/predict70',methods=['GET'])
def predict70():
    pkl70_file=open('gphSALES.pkl', 'rb')
    mydict70=pickle.load(pkl70_file)
    pkl70_file.close( )

    return jsonify({"Result70": mydict70})

@app.route('/predict18',methods=['GET'])
def predict18():
    pkl18_file=open('Sales1.pkl', 'rb')
    mydict18=pickle.load(pkl18_file)
    pkl18_file.close( )

    return jsonify({"Result18": mydict18})

@app.route('/predict19',methods=['GET'])
def predict19():
    pkl19_file=open('Sales2.pkl', 'rb')
    mydict19=pickle.load(pkl19_file)
    pkl19_file.close( )

    return jsonify({"Result19": mydict19})

@app.route('/predict71',methods=['GET'])
def predict71():
    pkl71_file=open('gphACNB.pkl', 'rb')
    mydict71=pickle.load(pkl71_file)
    pkl71_file.close( )

    return jsonify({"Result71": mydict71})

@app.route('/predict20',methods=['GET'])
def predict20():
    pkl20_file=open('ACNB1.pkl', 'rb')
    mydict20=pickle.load(pkl20_file)
    pkl20_file.close( )

    return jsonify({"Result20": mydict20})

@app.route('/predict21',methods=['GET'])
def predict21():
    pkl21_file=open('ACNB2.pkl', 'rb')
    mydict21=pickle.load(pkl21_file)
    pkl21_file.close( )

    return jsonify({"Result21": mydict21})

@app.route('/predict72',methods=['GET'])
def predict72():
    pkl72_file=open('gphTesla.pkl', 'rb')
    mydict72=pickle.load(pkl72_file)
    pkl72_file.close( )

    return jsonify({"Result72": mydict72})

@app.route('/predict22',methods=['GET'])
def predict22():
    pkl22_file=open('Tesla1.pkl', 'rb')
    mydict22=pickle.load(pkl22_file)
    pkl22_file.close( )

    return jsonify({"Result22": mydict22})

@app.route('/predict23',methods=['GET'])
def predict23():
    pkl23_file=open('Tesla2.pkl', 'rb')
    mydict23=pickle.load(pkl23_file)
    pkl23_file.close( )

    return jsonify({"Result23": mydict23})

@app.route('/predict73',methods=['GET'])
def predict73():
    pkl73_file=open('gphLucid.pkl', 'rb')
    mydict73=pickle.load(pkl73_file)
    pkl73_file.close( )

    return jsonify({"Result73": mydict73})

@app.route('/predict24',methods=['GET'])
def predict24():
    pkl24_file=open('Lucid1.pkl', 'rb')
    mydict24=pickle.load(pkl24_file)
    pkl24_file.close( )

    return jsonify({"Result24": mydict24})

@app.route('/predict25',methods=['GET'])
def predict25():
    pkl25_file=open('Lucid2.pkl', 'rb')
    mydict25=pickle.load(pkl25_file)
    pkl25_file.close( )

    return jsonify({"Result25": mydict25})

@app.route('/predict74',methods=['GET'])
def predict74():
    pkl74_file=open('gphToyo.pkl', 'rb')
    mydict74=pickle.load(pkl74_file)
    pkl74_file.close( )

    return jsonify({"Result74": mydict74})

@app.route('/predict26',methods=['GET'])
def predict26():
    pkl26_file=open('Toyota1.pkl', 'rb')
    mydict26=pickle.load(pkl26_file)
    pkl26_file.close( )

    return jsonify({"Result26": mydict26})

@app.route('/predict27',methods=['GET'])
def predict27():
    pkl27_file=open('Toyota2.pkl', 'rb')
    mydict27=pickle.load(pkl27_file)
    pkl27_file.close( )

    return jsonify({"Result27": mydict27})

@app.route('/predict75',methods=['GET'])
def predict75():
    pkl75_file=open('gphPola.pkl', 'rb')
    mydict75=pickle.load(pkl75_file)
    pkl75_file.close( )

    return jsonify({"Result75": mydict75})

@app.route('/predict28',methods=['GET'])
def predict28():
    pkl28_file=open('Polar1.pkl', 'rb')
    mydict28=pickle.load(pkl28_file)
    pkl28_file.close( )

    return jsonify({"Result28": mydict28})

@app.route('/predict29',methods=['GET'])
def predict29():
    pkl29_file=open('Polar2.pkl', 'rb')
    mydict29=pickle.load(pkl29_file)
    pkl29_file.close( )

    return jsonify({"Result29": mydict29})

@app.route('/predict76',methods=['GET'])
def predict76():
    pkl76_file=open('gphCanoo.pkl', 'rb')
    mydict76=pickle.load(pkl76_file)
    pkl76_file.close( )

    return jsonify({"Result20": mydict20})

@app.route('/predict30',methods=['GET'])
def predict30():
    pkl30_file=open('Canoo1.pkl', 'rb')
    mydict30=pickle.load(pkl30_file)
    pkl30_file.close( )

    return jsonify({"Result30": mydict30})

@app.route('/predict31',methods=['GET'])
def predict31():
    pkl31_file=open('Canoo2.pkl', 'rb')
    mydict31=pickle.load(pkl31_file)
    pkl31_file.close( )

    return jsonify({"Result31": mydict31})

@app.route('/predict77',methods=['GET'])
def predict77():
    pkl77_file=open('gphFerari.pkl', 'rb')
    mydict77=pickle.load(pkl77_file)
    pkl77_file.close( )

    return jsonify({"Result77": mydict77})

@app.route('/predict32',methods=['GET'])
def predict32():
    pkl32_file=open('Ferari1.pkl', 'rb')
    mydict32=pickle.load(pkl32_file)
    pkl32_file.close( )

    return jsonify({"Result32": mydict32})

@app.route('/predict33',methods=['GET'])
def predict33():
    pkl33_file=open('Ferari2.pkl', 'rb')
    mydict33=pickle.load(pkl33_file)
    pkl33_file.close( )

    return jsonify({"Result33": mydict33})

@app.route('/predict78',methods=['GET'])
def predict78():
    pkl78_file=open('gphHonda.pkl', 'rb')
    mydict78=pickle.load(pkl78_file)
    pkl78_file.close( )

    return jsonify({"Result78": mydict78})

@app.route('/predict34',methods=['GET'])
def predict34():
    pkl34_file=open('Honda1.pkl', 'rb')
    mydict34=pickle.load(pkl34_file)
    pkl34_file.close( )

    return jsonify({"Result34": mydict34})

@app.route('/predict35',methods=['GET'])
def predict35():
    pkl35_file=open('Honda2.pkl', 'rb')
    mydict35=pickle.load(pkl35_file)
    pkl35_file.close( )

    return jsonify({"Result35": mydict35})

@app.route('/predict79',methods=['GET'])
def predict79():
    pkl79_file=open('gphHyun.pkl', 'rb')
    mydict79=pickle.load(pkl79_file)
    pkl79_file.close( )

    return jsonify({"Result79": mydict79})

@app.route('/predict36',methods=['GET'])
def predict36():
    pkl36_file=open('Hyundai1.pkl', 'rb')
    mydict36=pickle.load(pkl36_file)
    pkl36_file.close( )

    return jsonify({"Result36": mydict36})

@app.route('/predict37',methods=['GET'])
def predict37():
    pkl37_file=open('Hyundai2.pkl', 'rb')
    mydict37=pickle.load(pkl37_file)
    pkl37_file.close( )

    return jsonify({"Result37": mydict37})

@app.route('/predict80',methods=['GET'])
def predict80():
    pkl80_file=open('gphDis.pkl', 'rb')
    mydict80=pickle.load(pkl80_file)
    pkl80_file.close( )

    return jsonify({"Result80": mydict80})

@app.route('/predict38',methods=['GET'])
def predict38():
    pkl38_file=open('Disney1.pkl', 'rb')
    mydict38=pickle.load(pkl38_file)
    pkl38_file.close( )

    return jsonify({"Result38": mydict38})

@app.route('/predict39',methods=['GET'])
def predict39():
    pkl39_file=open('Disney2.pkl', 'rb')
    mydict39=pickle.load(pkl39_file)
    pkl39_file.close( )

    return jsonify({"Result39": mydict39})

@app.route('/predict81',methods=['GET'])
def predict81():
    pkl81_file=open('gphNet.pkl', 'rb')
    mydict81=pickle.load(pkl81_file)
    pkl81_file.close( )

    return jsonify({"Result81": mydict81})

@app.route('/predict40',methods=['GET'])
def predict40():
    pkl40_file=open('Netflix1.pkl', 'rb')
    mydict40=pickle.load(pkl40_file)
    pkl40_file.close( )

    return jsonify({"Result40": mydict40})

@app.route('/predict41',methods=['GET'])
def predict41():
    pkl41_file=open('Netflix2.pkl', 'rb')
    mydict41=pickle.load(pkl41_file)
    pkl41_file.close( )

    return jsonify({"Result41": mydict41})

@app.route('/predict82',methods=['GET'])
def predict82():
    pkl82_file=open('gphFubo.pkl', 'rb')
    mydict82=pickle.load(pkl82_file)
    pkl82_file.close( )

    return jsonify({"Result82": mydict82})

@app.route('/predict42',methods=['GET'])
def predict42():
    pkl42_file=open('Fubo1.pkl', 'rb')
    mydict42=pickle.load(pkl42_file)
    pkl42_file.close( )

    return jsonify({"Result42": mydict42})

@app.route('/predict43',methods=['GET'])
def predict43():
    pkl43_file=open('Fubo2.pkl', 'rb')
    mydict43=pickle.load(pkl43_file)
    pkl43_file.close( )

    return jsonify({"Result43": mydict43})

#@app.route('/predict83',methods=['GET'])
#def predict83():
 #   pkl83_file=open('gphRoku.pkl', 'rb')
  #  mydict83=pickle.load(pkl83_file)
   # pkl83_file.close( )

    #return jsonify({"Result83": mydict83})

@app.route('/predict44',methods=['GET'])
def predict44():
    pkl44_file=open('Roku1.pkl', 'rb')
    mydict44=pickle.load(pkl44_file)
    pkl44_file.close( )

    return jsonify({"Result44": mydict44})

@app.route('/predict45',methods=['GET'])
def predict45():
    pkl45_file=open('Roku2.pkl', 'rb')
    mydict45=pickle.load(pkl45_file)
    pkl45_file.close( )

    return jsonify({"Result45": mydict45})

@app.route('/predict84',methods=['GET'])
def predict84():
    pkl84_file=open('gphZnga.pkl', 'rb')
    mydict84=pickle.load(pkl84_file)
    pkl84_file.close( )

    return jsonify({"Result84": mydict84})

@app.route('/predict46',methods=['GET'])
def predict46():
    pkl46_file=open('Znga1.pkl', 'rb')
    mydict46=pickle.load(pkl46_file)
    pkl46_file.close( )

    return jsonify({"Result46": mydict46})

@app.route('/predict47',methods=['GET'])
def predict47():
    pkl47_file=open('Znga2.pkl', 'rb')
    mydict47=pickle.load(pkl47_file)
    pkl47_file.close( )

    return jsonify({"Result47": mydict47})

if __name__ == '__main__':
    app.run(debug=True)




