

export default function (){};

export function rutValidator () {
    let rutCompleto = this.form.rut
    if (rutCompleto == 0){
      return null
    }
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
      return false;
    let tmp 	= rutCompleto.split('-');
    let digv	= tmp[1]; 
    let rut 	= tmp[0];
    if ( digv == 'K' ) digv = 'k' ;
    
    let M=0,S=1;
    for(;rut;rut=Math.floor(rut/10))
      S=(S+rut%10*(9-M++%6))%11;
    return ((S?S-1:'k') == digv) ? true : false
  }

export function emailValidator() {
    if (this.form.correo == "" ){
      return null
    }
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(this.form.correo).toLowerCase());
  };

export function yearsValidator() {
    if (this.form.edad == "" ){
      return null
    }
    const numbers = /^[0-9]+$/
    if (numbers.test(this.form.edad)){
      return parseInt(this.form.edad)>= 18 ? true: false;
    }
    return false
  };

export function nameValidator(){
    if (this.form.nombre == "" ){
      return null
    }
    const letters = /^[A-Za-zá-ú]+$/
    return letters.test(this.form.nombre)
  };

export function lastname1Validator(){
    if (this.form.apellidoPaterno == "" ){
      return null
    }
    const letters = /^[A-Za-zá-ú]+$/
    return letters.test(this.form.apellidoPaterno)
  };

export function lastname2Validator(){
    if (this.form.apellidoMaterno == "" ){
      return null
    }
    const letters = /^[A-Za-zá-ú]+$/
    return letters.test(this.form.apellidoMaterno)
  };

export function dateValidator(){
    if (this.form.fecha == "" ){
      return null
    }
    let now = new Date()
    return now < new Date(this.form.fecha)? true : false
  };

export function selectValidator(){
    return this.form.sexo && this.form.hora && this.form.medico
  };