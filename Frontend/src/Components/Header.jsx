import React from 'react';
import { Wifi } from 'lucide-react';

const Header = () => {
  return (
    <header className="bg-telco-light-blue p-4 shadow-lg flex items-center justify-between">
      <div className="flex items-center space-x-3">
        <Wifi className="text-telco-green h-8 w-8" />
        <h1 className="text-2xl font-bold text-telco-white tracking-wider">
          Telco Network Simulation Platform
        </h1>
      </div>
      <span className="text-xs text-telco-slate">Control Panel v0.1</span>
    </header>
  );
};

export default Header;