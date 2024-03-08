

_ = ( ...v ) => console.log( ...v );

class siren {
   constructor( props ) {
      this.cp = !props || !props.cp ? 12859 
         : props.cp;
      this.draws = [
         20,   50,   90,   160,  280, 
         440,  680,  1100, 1700, 2700,
      ];
      this.cpDepoisDaS = 5639;
      this.cpDepoisDaC = 1229;
      this.coin = 1310;
      this.custoDaSiren = this.cp - this.cpDepoisDaS;
      this.custoDaCoin = `${this.coin} coin: ${ this.cpDepoisDaS - this.cpDepoisDaC } cp`;   
      this.custoDaDraw = this.draws.reduce(
         ( x, y ) => x + y
      );

      _( this );
   }
   
}

new siren();

