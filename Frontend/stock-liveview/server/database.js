const { MongoClient } = require("mongodb");

let client;

const initializeMongoDB = async () => {
  const url =
    process.env.MONGODB_URL ||
    "mongodb://mongo0:27017,mongo1:27018,mongo2:27019/?replicaSet=rs0";
  client = new MongoClient(url);
  console.log(`Connecting to MongoDB at ${url}`);
  await client.connect();
  console.log("Connected to MongoDB");
};

const getMongoClient = () => {
  return client;
};

module.exports = { initializeMongoDB, getMongoClient };
