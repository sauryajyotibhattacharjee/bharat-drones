const Team = () => {
    const members = [
      { name: "Shaik Sameer Pasha", role: "CEO - Hardware Developer" },
      { name: "Saurajyoti Bhattacharjee", role: "COO - Software & AI Expert" },
      { name: "Dr. C. Muralidharan", role: "Design Expert - Project Manager" },
      { name: "Dr.V. Arulalan", role: "IoT Specialist - Project Manager" },
      {name: "Mr . Mahesh Kumar Hota", role: "Executive Support- Aviation Expert"},
      {name: "Mr . Abishek Sinha", role: "Executive Support- Business Mentor"},
      {name: "Yash Jha", role: "Developer"},
    ];
  
    return (
      <div className="p-8">
        <h2 className="text-3xl font-bold text-gray-800">Meet Our Team</h2>
        <div className="mt-4 space-y-4">
          {members.map((member, index) => (
            <div key={index} className="p-4 bg-gray-100 rounded-md">
              <h3 className="text-xl font-semibold">{member.name}</h3>
              <p className="text-gray-600">{member.role}</p>
            </div>
          ))}
        </div>
      </div>
    );
  };
  
  export default Team;
  