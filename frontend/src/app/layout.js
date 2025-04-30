import './globals.css';
import Header from '@/app/components/Header';

export default function Layout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-800">
        <div className="min-h-screen flex flex-col">
          <Header />
          <main className="flex-grow container mx-auto px-4 py-8">{children}</main>
          <footer className="text-center text-sm text-gray-500 py-4">
            &copy; {new Date().getFullYear()} Business Advisor AI
          </footer>
        </div>
      </body>
    </html>
  );
}

