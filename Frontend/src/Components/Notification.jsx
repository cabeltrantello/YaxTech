import React, { useEffect } from 'react';
import { CheckCircle, AlertTriangle } from 'lucide-react';

const Notification = ({ message, type, onClose }) => {
  if (!message) return null;

  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, 5000); // Auto-close after 5 seconds

    return () => clearTimeout(timer);
  }, [message, onClose]);

  const isSuccess = type === 'success';
  const bgColor = isSuccess ? 'bg-green-500' : 'bg-red-500';
  const Icon = isSuccess ? CheckCircle : AlertTriangle;

  return (
    <div className={`fixed bottom-5 right-5 text-white p-4 rounded-lg shadow-xl flex items-center space-x-4 ${bgColor}`}>
      <Icon className="h-6 w-6" />
      <span>{message}</span>
      <button onClick={onClose} className="font-bold text-xl">&times;</button>
    </div>
  );
};

export default Notification;
