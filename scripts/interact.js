const dotenv = require('dotenv');
const { TezosToolkit } = require('@taquito/taquito');
const { InMemorySigner } = require('@taquito/signer');

dotenv.config();

const { RPC_URL, PRIVATE_KEY, CONTRACT_ADDRESS } = process.env;

async function add_spekun(id_sepeda, node) {
  const signer = await InMemorySigner.fromSecretKey(PRIVATE_KEY);
  const Tezos = new TezosToolkit(RPC_URL);
  Tezos.setProvider({ signer: signer });

  const contract = await Tezos.contract.at(CONTRACT_ADDRESS);

  const tx = await contract.methods.add_sepeda(id_sepeda = id_sepeda, node = node).send();

  console.log(await tx.confirmation(1));
}

async function pinjam_spekun(id_sepeda, peminjam) {
  const signer = await InMemorySigner.fromSecretKey(PRIVATE_KEY);
  const Tezos = new TezosToolkit(RPC_URL);
  Tezos.setProvider({ signer: signer });

  const contract = await Tezos.contract.at(CONTRACT_ADDRESS);

  const tx = await contract.methods.borrow_sepeda(id_sepeda = id_sepeda, peminjam = peminjam).send();

  console.log(await tx.confirmation(1));
}

async function kembalikan_spekun(id_sepeda, peminjam, node) {
  const signer = await InMemorySigner.fromSecretKey(PRIVATE_KEY);
  const Tezos = new TezosToolkit(RPC_URL);
  Tezos.setProvider({ signer: signer });

  const contract = await Tezos.contract.at(CONTRACT_ADDRESS);

  const tx = await contract.methods.return_sepeda(id_sepeda = id_sepeda, node = node, peminjam = peminjam).send();

  console.log(await tx.confirmation(1));
}