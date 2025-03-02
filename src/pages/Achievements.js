const Achievements = () => {
    const achievements = [
      {
        title: "Winner of Ideation Hackathon, Tripura (2024)",
        description:
          "Bharat Drone Innovations won the Ideation Hackathon for its groundbreaking organ delivery drone project.",
      },
      {
        title: "Finalist in Startup Challenge, 3DPCOE Hackathon (2024, Guwahati)",
        description:
          "We showcased our precision agriculture and defense drone technologies, earning a finalist position.",
      },
      {
        title: "Drone Model Showcased at IMC 2024",
        description:
          "Our drone model was featured at the Indian Mobile Congress, recognized for applications in defense, agriculture, and healthcare.",
      },
      {
        title: "Recognized for Innovations in Defense, Agriculture, and Healthcare",
        description:
          "Our AI-powered autonomous drones are setting new benchmarks in critical sectors.",
      },
    ];
  
    return (
      <div className="p-10">
        <h2 className="text-3xl font-bold text-gray-800 text-center">Our Achievements</h2>
        <div className="mt-6 space-y-6">
          {achievements.map((achievement, index) => (
            <div
              key={index}
              className="p-6 bg-gray-100 rounded-lg shadow-lg hover:shadow-xl transition"
            >
              <h3 className="text-xl font-semibold text-primary">{achievement.title}</h3>
              <p className="mt-2 text-gray-600">{achievement.description}</p>
            </div>
          ))}
        </div>
      </div>
    );
  };
  
  export default Achievements;
  