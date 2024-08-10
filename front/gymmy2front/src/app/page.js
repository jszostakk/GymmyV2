import React from 'react';

export default async function Page() {
  const res = await fetch('http:/172.17.0.2:80/');
  const data = await res.json();
  console.log(data);
  return (
    <div>
      <h1>{data.message}</h1>
    </div>
  );
}
