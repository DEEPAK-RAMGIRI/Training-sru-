
// const data = {
//     "keys": {
//         "n": 4,
//         "k": 3
//     },
//     "1": { "base": "10", "value": "4" },
//     "2": { "base": "2", "value": "111" },
//     "3": { "base": "10", "value": "12" },
//     "6": { "base": "4", "value": "213" }
// };


const data = {
"keys": {
    "n": 10,
    "k": 7
  },
  "1": {
    "base": "6",
    "value": "13444211440455345511"
  },
  "2": {
    "base": "15",
    "value": "aed7015a346d635"
  },
  "3": {
    "base": "15",
    "value": "6aeeb69631c227c"
  },
  "4": {
    "base": "16",
    "value": "e1b5e05623d881f"
  },
  "5": {
    "base": "8",
    "value": "316034514573652620673"
  },
  "6": {
    "base": "3",
    "value": "2122212201122002221120200210011020220200"
  },
  "7": {
    "base": "3",
    "value": "20120221122211000100210021102001201112121"
  },
  "8": {
    "base": "6",
    "value": "20220554335330240002224253"
  },
  "9": {
    "base": "12",
    "value": "45153788322a1255483"
  },
  "10": {
    "base": "7",
    "value": "1101613130313526312514143"
  }
}

const n = data.keys.n;
const k = data.keys.k;


let shares = [];
for (const key in data) {
    if (key === 'keys') continue;
    const obj = data[key];
    shares.push({
        x: parseInt(key),
        value: BigInt(parseInt(obj.value, parseInt(obj.base)))
    });
}

const selectedShares = shares.slice(0, k);

function reconstructSecret(shares) {
    let secret = 0n;

    for (let i = 0; i < shares.length; i++) {
        const xi = BigInt(shares[i].x);
        const yi = shares[i].value;

        let num = 1n;
        let den = 1n;

        for (let j = 0; j < shares.length; j++) {
            if (i !== j) {
                const xj = BigInt(shares[j].x);
                num *= -xj;          
                den *= (xi - xj);    
            }
        }

        secret += yi * num / den;
    }

    return secret;
}


const secret = reconstructSecret(selectedShares);
console.log("Recovered Secret (constant term):", secret.toString());
