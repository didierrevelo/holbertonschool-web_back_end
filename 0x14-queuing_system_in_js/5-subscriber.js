import redis from 'redis';

  const subscriber = redis.createClient();

  subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  subscriber.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
  });

  const Channel = 'holberton school channel';
  subscriber.subscribe(Channel);

  subscriber.on('message', (channel, message) => {
    if (channel === Channel) {
      console.log(message);
    }

    if (message === 'KILL_SERVER') {
      subscriber.unsubscribe(Channel);
      subscriber.quit();
    }
  });
