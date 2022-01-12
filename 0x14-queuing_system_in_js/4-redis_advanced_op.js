import redis from 'redis';

  const client = redis.createClient();

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
  });

  const KEY = 'HolbertonSchools';

  const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
  const values = [50, 80, 20, 20, 40, 2];

  keys.forEach((key, index) => {
    console.log(redis.print);
    client.hset(KEY, key, values[index], redis.print);
  });

  client.hgetall(KEY, (err, value) => {
    console.log(value);
  });
