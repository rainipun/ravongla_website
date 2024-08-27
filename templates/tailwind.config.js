/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./dist/*.html','./*.html'],
  theme: {
   
      colors:{
        'rs-green':'#024d27',
        'rs-green-c':'#27024d',
        'rs-green-c2':'#4d2702',
        'rs-beige':'#ded5af',
        'rs-white':'#ffffff',
        'rs-beige-c':'#afded5',
        'rs-beige-c2':'#d5afde',
      },
      fontFamily :{ 
        'pb': ['poppins-bold'], 
        'psb': ['poppins-SemiBold'],
        'pl':['poppins-light'],
      },
  },
  plugins: [],
}

