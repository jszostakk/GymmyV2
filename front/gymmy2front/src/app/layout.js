import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function Layout({ children }) {
  return (
    <html>
      <head>
        <title>My Next.js App</title>
      </head>
      <body>{children}</body>
    </html>
  );
}

