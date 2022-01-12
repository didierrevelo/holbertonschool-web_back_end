export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }

  const queueName = 'push_notification_code_3';

  jobs.forEach((format) => {
    const job = queue.create(queueName, format).save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    job.on('failed', () => {
      console.log(`Notification job ${job.id} failed`);
    });
  });
};
