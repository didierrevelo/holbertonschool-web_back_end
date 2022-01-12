import kue from 'kue';

const queue = kue.createQueue();

const format = {
  phoneNumber: '3135815880',
  message: 'This is your verification code',
}

const nameQueue = 'push_notification_code';

const job = queue.create(nameQueue, format).save((err) =>{
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('faile', () => {
  console.log('Notification job failed');
});
