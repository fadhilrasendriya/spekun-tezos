const dotenv = require('dotenv');
const { TezosToolkit } = require('@taquito/taquito');
const { InMemorySigner } = require('@taquito/signer');

dotenv.config();

const deploy = async () => {
  const { RPC_URL, PRIVATE_KEY } = process.env;

  const signer = await InMemorySigner.fromSecretKey(PRIVATE_KEY);
  const Tezos = new TezosToolkit(RPC_URL);
  Tezos.setProvider({ signer: signer });

  try {
    const { hash, contractAddress } = await Tezos.contract.originate({
      code: require('../compilation/Spekun/step_002_cont_0_contract.json'),
      init: require('../compilation/Spekun/step_002_cont_0_storage.json')
    });

    console.log(`success deployed to: ${contractAddress}`);

  } catch (error) {
    console.log(error);
  }
}

deploy();