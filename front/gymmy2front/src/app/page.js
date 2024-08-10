"use client"; // Add this line at the top

import { useEffect } from 'react';
import { useRouter } from 'next/navigation'; // Use 'next/navigation' instead of 'next/router'

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    const isAuthenticated = localStorage.getItem('isAuthenticated');

    if (!isAuthenticated) {
      router.push('/login');
    }
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('isAuthenticated');
    router.push('/login');
  };

  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      <p>You are logged in!</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}
